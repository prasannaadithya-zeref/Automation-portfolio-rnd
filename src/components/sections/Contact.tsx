import { motion } from "framer-motion"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Input } from "@/components/ui/input" // Need to create Input
import { Textarea } from "@/components/ui/textarea" // Need to create Textarea
import { Send } from "lucide-react"

export const Contact = () => {
    return (
        <section id="contact" className="py-20 scroll-mt-16">
            <motion.div
                initial={{ opacity: 0, scale: 0.95 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5 }}
                className="max-w-2xl mx-auto"
            >
                <Card>
                    <CardHeader className="text-center">
                        <CardTitle className="text-2xl">Get in Touch</CardTitle>
                        <CardDescription>
                            Have a project in mind or want to discuss automation? Send me a message.
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="space-y-2">
                                    <label htmlFor="name" className="text-sm font-medium">Name</label>
                                    <Input id="name" placeholder="John Doe" />
                                </div>
                                <div className="space-y-2">
                                    <label htmlFor="email" className="text-sm font-medium">Email</label>
                                    <Input id="email" type="email" placeholder="john@example.com" />
                                </div>
                            </div>
                            <div className="space-y-2">
                                <label htmlFor="message" className="text-sm font-medium">Message</label>
                                <Textarea id="message" placeholder="Tell me about your project..." className="min-h-[120px]" />
                            </div>
                            <Button type="submit" className="w-full gap-2">
                                Send Message <Send className="h-4 w-4" />
                            </Button>
                        </form>
                    </CardContent>
                </Card>
            </motion.div>
        </section>
    )
}
